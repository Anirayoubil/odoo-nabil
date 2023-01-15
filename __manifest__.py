# -*- coding: utf-8 -*-
{
    'name': "Hospital Management",
    'sequence': 1,
    'summary': """
        A hospital management module.""",

    'description': """
        A hospital management module for creating patient, doctor, 
        department, medical test, and appointments.
    """,

    'author': "Oumellahni Nabil",
    'website': "http://www.ensah.com",
    'category': 'Services',
    'version': '0.1',
    'license': 'LGPL-3',
    # any module necessary for this one to work correctly
    'depends': ['base', 'hr'],

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'data/appointment_seq.xml',
        'wizard/create_appointment_view.xml',
        'wizard/appointment_report_view.xml',
        'views/patient_view.xml',
        'views/doctor_view.xml',
        'views/department_view.xml',
        'views/appointment_view.xml',
        'views/medicaltest_view.xml',
        'reports/report.xml',
        'reports/appointment_report.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
