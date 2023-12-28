import allure


def microservice(name):
    return allure.label("msrv", name)


def owner(name):
    return allure.label("owner", name)


def layer(name):
    return allure.label("layer", name)
