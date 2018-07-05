#!/usr/bin/env python3

import mailroom_6 as m6

def clear_donations(donor_name):
    m6.DonationTable.delete().where(m6.DonationTable.fld_donor == donor_name).execute()

def test_donor():
    clear_donations('Kristian Francisco')
    kf = m6.Donor('Kristian Francisco', [1000, 100])
    test_metrics = kf.metrics()
    assert kf.name == 'Kristian Francisco'
    assert test_metrics[0] == 2
    assert test_metrics[1] == 1100
    assert test_metrics[2] == 550.0
    clear_donations('Kristian Francisco')

def test_donor_handle():
    clear_donations('Kristian Francisco')
    kf = m6.Donor('Kristian Francisco', [1000, 100])
    dh = m6.DonorHandler()
    dh.add_donor(kf)
    assert 'Kristian Francisco' in dh.donors
    assert dh.donors['Kristian Francisco'].donations == [1000, 100]
    clear_donations('Kristian Francisco')

def test_donor_challenge():
    clear_donations('Kristian Francisco')
    clear_donations('Kristian Francisco Projection')
    kf = m6.Donor('Kristian Francisco', [5, 1000, 100])
    dh = m6.DonorHandler()
    dh.add_donor(kf)
    dh2 = dh.dnr_challenge(factor=4, min_donation=10, max_donation=1000)
    print(dh2.donors['Kristian Francisco Projection'].donations)
    assert dh2.donors['Kristian Francisco Projection'].donations == [400]
    # assert False
    clear_donations('Kristian Francisco')
    clear_donations('Kristian Francisco Projection')

def test_donor_projection():
    clear_donations('Kristian Francisco')
    clear_donations('Kristian Francisco Projection')
    kf = m6.Donor('Kristian Francisco', [20, 1000, 100])
    dh = m6.DonorHandler()
    dh.add_donor(kf)
    prj_1 = dh.dnr_projections('Kristian Francisco Projection', factor=4, min_donation=10, max_donation=1000)
    assert prj_1 == 480
    clear_donations('Kristian Francisco')
    clear_donations('Kristian Francisco Projection')
