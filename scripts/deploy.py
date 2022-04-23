from scripts.helpful_scripts import get_account
from brownie import FundMe

def deploy_fund_me():
    account = get_account()
    fund_me = FundMe.deploy({"from":account}, publish_source=True)
    print(f"Contract deployed to {fund_me.address}")

def main():
    deploy_fund_me() 