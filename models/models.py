# -*- coding: utf-8 -*-

from datetime import datetime
from odoo import api
from odoo import fields
from odoo import models
from odoo.exceptions import ValidationError

# The shifts have a starting and ending date. A shift is assigned to many different
# employees. A shift is assigned to a zone.
class Shift(models.Model):
	_name = 'shiftmanagement.shift'

	init_date = fields.Datetime(string="Shift starting date", required=True)
	end_date = fields.Datetime(string="Shift ending date", required=True)

	employees = fields.Many2many('res.users', string='Employees')
	zone = fields.Many2one('shiftmanagement.zone', ondelete='set null', string='Zone', required=True, domain=['|',('name','=','Caja'),('name','=','Almacen')])

	@api.onchange('shift', 'init_date')
	def _verify_starting_date(self):
		if self.init_date and (self.init_date < str(datetime.today())):
			return {
				'warning':{
					'title':"Old starting date value",
					'message':"The starting date is in the past.", 
				},
			}
	@api.onchange('shift', 'end_date')
	def _verify_end_date(self):
		if self.end_date and (self.end_date < str(datetime.today())):
			return {
				'warning':{
					'title':"Old ending date value",
					'message':"The ending date is in the past.", 
				},
			}

	@api.constrains('shift', 'init_date', 'end_date')
	def _check_end_date(self):
		for record in self:
			if record.init_date > record.end_date:
				raise ValidationError("The starting date can't be later than the ending date.")
	
# Zones have a zone name and a manager. One zone can be assigned to many different
# shifts.
class Zone(models.Model):
	_name = 'shiftmanagement.zone'

	name = fields.Text(string="Name", required=True)

	shifts = fields.One2many('shiftmanagement.shift', 'zone', ondelete='set null', string='Shifts', required=True)
	
# Employees extend from odoo's user class. Each employee has a full name,
# a phone number and an email. An employee has assigned many different shifts.
class Employee(models.Model):
	_inherit = 'res.users'

	shifts = fields.Many2many('shiftmanagement.shift', string="Shifts")