# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo.tests import common


class TestHrAttendance(common.TransactionCase):

    def setUp(self):
        super(TestHrAttendance, self).setUp()
        self.ht_attendance_model = self.env['ht.attendance']
        # create attendance_1
        self.attendance_1 = self._create_hr_attendance(1, '2020-01-01', False)
        # create attendance_2
        self.attendance_2 = self._create_hr_attendance(1, '2020-01-01', False)        

    def _create_hr_attendance(self, employee_id, check_in, check_out):
        hr_attendance = self.ht_attendance_model.create({
            'employee_id': employee_id,
            'check_in': check_in,
            'check_out': check_out
        })
        return hr_attendance

    def test_hr_attendance_without_check_out(self):
        ids = self.ht_attendance_model.search(
            [
                ('employee_id', '=', '1'),
                ('check_in', '=', '2020-01-01'),
                ('check_out', '=', False)
            ]
        )
        self.assertEqual(
            len(ids),
            2,
            'Existen 2 registros sin salida para el mismo empleado'
        )
