import logging

import algokit_utils
from algosdk.v2client.algod import AlgodClient
from algosdk.v2client.indexer import IndexerClient

logger = logging.getLogger(__name__)


# define deployment behaviour based on supplied app spec
def deploy(
    algod_client: AlgodClient,
    indexer_client: IndexerClient,
    app_spec: algokit_utils.ApplicationSpecification,
    deployer: algokit_utils.Account,
) -> None:
    from smart_contracts.artifacts.calculator.calculator_client import (
        CalculatorClient,
    )

    testnetAlgodClient=AlgodClient("a"*64,"https://testnet-api.algonode.cloud")
    testnetIndexerClient=IndexerClient("a"*64,"https://testnet-idx.algonode.cloud")
    myAccount = algokit_utils.get_account_from_mnemonic("sausage warrior aunt funny bus tree canal submit pupil burger weasel leg clutch bubble outdoor doll group focus artwork reflect day wait ethics ability speed")

    app_client = CalculatorClient(
        algod_client=testnetAlgodClient,
        creator=myAccount,
        indexer_client=testnetIndexerClient,
    )

    app_client.deploy(
        on_schema_break=algokit_utils.OnSchemaBreak.AppendApp,
        on_update=algokit_utils.OnUpdate.AppendApp,
    )

    logger.info(f"Deployed Calculator With App ID: {app_client.app_id}")
    a=10
    b=5
    response = app_client.add(a=a,b=b)
    logger.info(
        f"Called add on {app_spec.contract.name} ({app_client.app_id}) "
        f"with a={a} and b={b}, received: {response.return_value}"
    )

    a=35
    b=7
    response = app_client.sub(a=a,b=b)
    logger.info(
        f"Called add on {app_spec.contract.name} ({app_client.app_id}) "
        f"with a={a} and b={b}, received: {response.return_value}"
    )

    a=27
    b=8
    response = app_client.mul(a=a,b=b)
    logger.info(
        f"Called add on {app_spec.contract.name} ({app_client.app_id}) "
        f"with a={a} and b={b}, received: {response.return_value}"
    )

    a=10
    b=5
    response = app_client.div(a=a,b=b)
    logger.info(
        f"Called add on {app_spec.contract.name} ({app_client.app_id}) "
        f"with a={a} and b={b}, received: {response.return_value}"
    )
