#!/usr/bin/env python

"""

"""

from donor_donation_model import *
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def num_donation():
    query = (Donor
             .select(Donor, fn.COUNT(Donation.amount).alias('donation_count'))
             .join(Donation, JOIN.LEFT_OUTER)
             .group_by(Donor)
             .order_by(Donor.donor_id))

    for donor in query:
        logger.info(f'Donor id {donor.donor_id} with name {donor.donor_name} has made {donor.donation_count} times donation')

def dotal_donation():
    query = (Donor
             .select(Donor, fn.SUM(Donation.amount).alias('donation_total'))
             .join(Donation, JOIN.LEFT_OUTER)
             .group_by(Donor)
             .order_by(Donor.donor_id))
    for donor in query:
        logger.info(f'Donor id {donor.donor_id} with name {donor.donor_name} has made ${donor.donation_total} in total')


def last_donation():
    query = (Donor
             .select(Donor, Donation.amount.alias('last_amount'), fn.MAX(Donation.donation_time).alias('last_time'))
             .join(Donation)
             .group_by(Donation.donation_donorid)
             .order_by(Donation.donation_donorid))
    for donor in query:
        logger.info(f'Donor id {donor.donor_id} with name {donor.donor_name} latest donation is ${donor.donation.last_amount}')

def average_donation():
    query = (Donor
             .select(Donor, fn.AVG(Donation.amount).alias('donation_average'))
             .join(Donation, JOIN.LEFT_OUTER)
             .order_by(Donor.donor_id))

    for donor in query:
        logger.info(f'Donor id {donor.donor_id} with name {donor.donor_name} average donation is ${donor.donation_average}')


num_donation()
dotal_donation()
last_donation()
average_donation()

database.close()


# def main():
#     selection_dict = {"1": send_thank_you,
#                       "2": print_donor_report,
#                       "3": db.save_letters_to_disk,
#                       "4": quit}
#
#     while True:
#         selection = main_menu_selection()
#         try:
#             selection_dict[selection]()
#         except KeyError:
#             print("error: menu selection is invalid!")
#
# if __name__ == "__main__":
#
#     main()
