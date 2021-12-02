#!/usr/sh

# make locale dir

mkdir -p he
mkdir -p sv

# sane-pygtk

intltool-extract --type=gettext/glade sane-pygtk.glade
xgettext --language=Python --keyword=_ --keyword=N_ --output=sane-pygtk.pot sane-pygtk sane-pygtk.glade.h

if ( test -e he_sane-pygtk.po ); then
  msgmerge --update he_sane-pygtk.po sane-pygtk.pot
else
  msginit --input=sane-pygtk.pot --output he_sane-pygtk.po --locale=he_IL.utf-8
fi

if ( test -e he_sane-pygtk.po ); then
  msgmerge --update sv_sane-pygtk.po sane-pygtk.pot
else
  msginit --input=sane-pygtk.pot --output sv_sane-pygtk.po --locale=sv_SE.utf-8
fi

msgfmt --output-file=he/sane-pygtk.mo he_sane-pygtk.po
msgfmt --output-file=sv/sane-pygtk.mo sv_sane-pygtk.po
