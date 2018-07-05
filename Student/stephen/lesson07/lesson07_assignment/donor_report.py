"""
Module for creating a report
"""

from donor_model import *

def create_report():
    """
    Creates report print-out
    """
    donor_donations = (
            Donation.select(
                Donation.donor_id,
                Donor.first_name,
                Donor.last_name,
                fn.SUM(Donation.amount).alias('total_given'),
                fn.COUNT(Donation.id).alias('num_gifts'),
                fn.AVG(Donation.amount).alias('average_gift')
                )
            .join(Donor, JOIN.INNER)
            .group_by(Donation.donor_id, Donor.first_name, Donor.last_name)
            .order_by(fn.SUM(Donation.amount).desc())
        )

    report_rows = []
    for d in donor_donations:
        name = d.donor_id.first_name + ' ' + d.donor_id.last_name
        report_rows.append('{:26s} {:>12s} {:^13d} {:>12s}'.format(name, '${:,.2f}'.format(d.total_given), d.num_gifts, '${:,.2f}'.format(d.average_gift)))
    header = ('Donor Name                | Total Given | Num Gifts | Average Gift\n') + ('-' * 66) + '\n'
    return header + '\n'.join(report_rows) + '\n'

if __name__ == '__main__':
    print(create_report())
    database.close()