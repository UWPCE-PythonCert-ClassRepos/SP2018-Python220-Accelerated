from mailroom_meta import Donor, DonorDB


def test_donor_init():
    d = Donor('William Gates III')
    assert d.name == 'William Gates III'
    assert d.donations == []
    d.add_donation(10000)
    d.add_donation(20000)
    assert d.total_donations == 30000
    #assert print(d) and False


def test_donors():
    d = Donor('Paul Allen')
    d.add_donation(30000)

    db = DonorDB()
    db.add_donor(d)
    assert db.get_total_from_donor('Paul Allen') == 30000

    e = Donor('Jeff Bezos')
    e.add_donation(40000)
    e.add_donation(50000)

    db.add_donor(e)

    assert db.get_total_from_donor('Jeff Bezos') == 90000
    assert db.count_donors == 2
    assert db.count_donations == 3
    assert db.total_donations == 120000
    assert db.average_total_donation == 60000
    assert db.average_single_donation == 40000

    test_list = db.donor_list()
    assert test_list.startswith('Paul Allen')
    assert test_list.endswith('Jeff Bezos')

    # assert print(db) and False
