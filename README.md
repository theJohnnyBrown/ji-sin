ji-sin
======

Automatically create a dev environment on osx or linux for php or html development.
Currently ji-sin is in a very basic state, all it does is add the appropriate
entries to your /etc/hosts file and apache vhosts config.

This probably won't work unless you've already configured apache and php on your system. I wrote it
to easily add additional sites on a dev environment that is already properly configured.

## Usage

```bash
# create the directory where your website will live
mkdir ~/my-new-website
cd my-new-website
echo "<?php phpinfo(); ?>" > index.php

# BACKUP YOUR CONFIG FILES
cd /etc
sudo git init
sudo git add .
sudo git commit -m "config files should be version controlled."

# download and run ji-sin
cd ..
git clone git@github.com:theJohnnyBrown/ji-sin.git
cd ji-sin
sudo python ji-sin.py mysite.dev ~/my-new-website/
```

After the above commands, you should be able to get http://msyite.dev in your browser
and see the phpinfo page. From here you can treat `~/my-new-website` just like the htdocs
or public_html dir of a web server.

## TODO

 + Test on linux
 + Add code to verify that PHP and apache are installed and properly configured.
