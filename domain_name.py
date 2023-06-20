def domain_name(url):
    domain = url.replace('http://', '').replace('https://', '').replace('www.', '')
    domain = domain.split('.')
    return domain[0]

