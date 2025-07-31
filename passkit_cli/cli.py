import click

@click.group()
def cli():
    """PassKit command line interface."""

@cli.group()
def membership():
    """Membership related commands."""

@membership.command('create-program')
@click.option('--name', default='Quickstart Program', help='Program name')
def membership_create_program(name):
    from .membership.create_program import create_program
    program_id = create_program(name)
    click.echo(f'Created program: {program_id}')

@membership.command('enrol-member')
@click.option('--program-id', required=True)
@click.option('--tier-id', required=True)
@click.option('--forename', required=True)
@click.option('--surname', required=True)
@click.option('--email', required=True)
def membership_enrol_member(program_id, tier_id, forename, surname, email):
    from .membership.enrol_member import enrol_member
    member_id = enrol_member(program_id, tier_id, forename, surname, email)
    click.echo(f'Enrolled member: {member_id}')

@cli.group()
def coupons():
    """Coupon commands."""

@coupons.command('create')
@click.option('--campaign-id', required=True)
@click.option('--offer-id', required=True)
@click.option('--forename', required=True)
@click.option('--surname', required=True)
@click.option('--email', required=True)
def coupons_create(campaign_id, offer_id, forename, surname, email):
    from .coupons.create_coupon import create_coupon
    coupon_id = create_coupon(campaign_id, offer_id, forename, surname, email)
    click.echo(f'Created coupon: {coupon_id}')

if __name__ == '__main__':
    cli()

