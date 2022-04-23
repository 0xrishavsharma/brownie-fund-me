from scripts.helpful_scripts1 import (
    deploy_mocks,
    get_account,
    LOCAL_BLOCKCHAIN_ENVIRONMENTS,
)
from brownie import FundMe, network, config, MockV3Aggregator


def deploy_fund_me():
    account = get_account()
    # Passing the priceFeed address to our fundme contract by adding it in the deploy script.

    # If we are on a persistant rinkeby chain then use the associated(declared) address
    # otherwise, deploy mocks.
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        price_feed_address = config["networks"][network.show_active()]["eth_usd_price_feed"]

    else:
        deploy_mocks()
        price_feed_address = MockV3Aggregator[-1].address

    fund_me = FundMe.deploy(
        price_feed_address,
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify"),
    )
    print(f"Contract deployed to {fund_me.address}")
    return fund_me

def main():
    deploy_fund_me()
