import os, sys, shutil, mmap, subprocess

HOSTS_FILE = "/etc/hosts"
VHOSTS_FILE = "/etc/apache2/extra/httpd-vhosts.conf"

VHOSTS_TEMPLATE = """

<VirtualHost *:80>
    ServerAdmin webmaster@dummy-host.example.com
    DocumentRoot "{webroot}"
    ServerName {domain}
    # ServerAlias www.dummy-host.example.com
    ErrorLog "/private/var/log/apache2/{domain}-error_log"
    CustomLog "/private/var/log/apache2/{domain}-access_log" common
</VirtualHost>

<Directory "{webroot}">
    Options Indexes FollowSymLinks MultiViews
    AllowOverride All
    Order allow,deny
    Allow from all
</Directory>

"""


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print "usage: %s domainname.dev /path/to/webroot/" % sys.argv[0]
        sys.exit(1)

    domain, webroot = sys.argv[1:3]
    hosts_entry = "\n127.0.0.1\t%s\n" % domain

    with open(HOSTS_FILE) as hosts:
        s = mmap.mmap(hosts.fileno(), 0, access=mmap.ACCESS_READ)
        if s.find(domain.strip()) > 0:
            print "%s already has an entry in %s. Exiting." % (domain, HOSTS_FILE)
            sys.exit(1)

    with open(HOSTS_FILE, "a") as hosts:
        hosts.write(hosts_entry)

    with open(VHOSTS_FILE, "a") as vhosts:
        vhosts.write(VHOSTS_TEMPLATE.format(domain=domain, webroot=webroot))

    subprocess.call(["apachectl", "restart"])
        
    sys.exit(0)
