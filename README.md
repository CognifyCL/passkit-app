PassKit Python Quickstart
=======================

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Version](https://badge.fury.io/py/passkit-python-grpc-sdk.svg)](https://pypi.org/project/passkit-python-grpc-sdk/)

### Overview

This quickstart aims to help  get Python developers up and running with the PassKit SDK as quickly as possible.

### Prerequisites

You will need the following:

- A PassKit account (signup for free at https://app.passkit.com)
- Your PassKit SDK Credentials (available from the https://app.passkit.com/app/account/developer-tools)
- Python 3.7 or above from https://www.oracle.com/java/technologies/downloads/ (https://docs.oracle.com/en/java/javase/18/install/overview-jdk-installation.html - guide on how to download)
- Gradle Build Tool from https://gradle.org/install/ with guide on how to install

### Configuration

1. Download or clone this quickstart repository, create a folder `certs` in the resources folder of the repository and add the following three PassKit credential files:
    - certificate.pem
    - ca-chain.pem
    - key.pem
    
    You can disregard the key-java.pem credentials file as it is not compatible with Python.
2. Use `pip install passkit-python-grpc-sdk` to download the latest sdk from python.
    
###  Membership Cards
In the membership folder the methods there are:
- create-program.py - takes a new program name and creates a new program
- create-tier.py -  takes the programId of the program just created in the above program, creates a new template (based of default template), creates a tier, and links this tier to the program
- enrol-member.py - takes programId and tierId created by the above methods, and memberDetails, creates a new member record, and sends a welcome email to deliver membership card url
- update-member.py - takes memberId and memberDetails, and updates existing member record
- check-in-member.py - takes memberId and location details and checks in the selected member
- check-out-member.py - takes memberId and location details and checks out the selected member
- earn-points.py - takes a programId of an existing program and memberId of existing member to add points to chosen member
- burn-points.py - takes a programId of an existing program and memberId of existing member to use points from a chosen member
- delete-member.py - takes programId, tierId, memberId and memberDetails, deletes an existing member record

###  Coupons
In the coupons folder the methods are:
- create-campaign.py - takes a new campaign name and creates a new campaign
- create-offer.py - takes a campaignId of the campaign you just created and creates a new template (based of default template), creates an offer, and links this offer to the campaign
- create-coupon.py - takes campaignId and offerId created by the above methods, and couponDetails, creates a new coupon record, and sends a welcome email to deliver coupon card url
- list-coupons.py - takes campaignId and returns list of coupon records under that campaign
- update-coupon.py - takes a campaignId of an existing campaign and couponId of existing coupon to update that coupon
- redeem-coupon.py - takes a campaignId of an existing campaign and couponId of existing coupon to redeem that coupon
- void-coupon.py - takes the couponId, offerId and campaignId to void an existing coupon



## Documentation
* [PassKit Membership Official Documentation](https://docs.passkit.io/protocols/member)
* [PassKit Coupons Official Documentation](https://docs.passkit.io/protocols/coupon)
* [PassKit Events Official Documentation](https://docs.passkit.io/protocols/event-tickets/)


## CLI Usage

Install dependencies and the package:

```bash
pip install -e .
```

Set the required environment variables pointing to your certificate files and run commands:

```bash
export PASSKIT_CA_CHAIN=/path/to/ca.pem
export PASSKIT_CERT=/path/to/certificate.pem
export PASSKIT_KEY=/path/to/key.pem

passkit membership create-program --name "My Program"
```

Run `passkit --help` to see all available commands.
