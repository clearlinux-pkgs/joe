#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : joe
Version  : 4.6
Release  : 28
URL      : https://sourceforge.net/projects/joe-editor/files/JOE%20sources/joe-4.6/joe-4.6.tar.gz
Source0  : https://sourceforge.net/projects/joe-editor/files/JOE%20sources/joe-4.6/joe-4.6.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0 GPL-2.0+
Requires: joe-bin
Requires: joe-data
Requires: joe-doc
BuildRequires : ncurses-dev
BuildRequires : pkgconfig(ncurses)
Patch1: stateless.patch
Patch2: ncursesw.patch
Patch3: indent.patch
Patch4: crash.patch

%description
# Utility programs:
## Stringify
This converts rc and .jsf files into a C file.  Use it to build the builtins.c file with:

%package bin
Summary: bin components for the joe package.
Group: Binaries
Requires: joe-data

%description bin
bin components for the joe package.


%package data
Summary: data components for the joe package.
Group: Data

%description data
data components for the joe package.


%package doc
Summary: doc components for the joe package.
Group: Documentation

%description doc
doc components for the joe package.


%prep
%setup -q -n joe-4.6
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1515785534
%configure --disable-static --sysconfdir=/usr/share/defaults/
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1515785534
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/jmacs
/usr/bin/joe
/usr/bin/jpico
/usr/bin/jstar
/usr/bin/rjoe

%files data
%defattr(-,root,root,-)
/usr/share/applications/jmacs.desktop
/usr/share/applications/joe.desktop
/usr/share/applications/jpico.desktop
/usr/share/applications/jstar.desktop
/usr/share/defaults/joe/ftyperc
/usr/share/defaults/joe/jicerc.ru
/usr/share/defaults/joe/jmacsrc
/usr/share/defaults/joe/joerc
/usr/share/defaults/joe/joerc.zh_TW
/usr/share/defaults/joe/jpicorc
/usr/share/defaults/joe/jstarrc
/usr/share/defaults/joe/rjoerc
/usr/share/defaults/joe/shell.csh
/usr/share/defaults/joe/shell.sh
/usr/share/joe/charmaps/klingon
/usr/share/joe/colors/default.jcf
/usr/share/joe/colors/gruvbox.jcf
/usr/share/joe/colors/ir_black.jcf
/usr/share/joe/colors/molokai.jcf
/usr/share/joe/colors/solarized.jcf
/usr/share/joe/colors/wombat.jcf
/usr/share/joe/colors/xoria.jcf
/usr/share/joe/colors/zenburn-hc.jcf
/usr/share/joe/colors/zenburn.jcf
/usr/share/joe/lang/de.po
/usr/share/joe/lang/fr.po
/usr/share/joe/lang/ru.po
/usr/share/joe/lang/uk.po
/usr/share/joe/lang/zh_TW.po
/usr/share/joe/syntax/4gl.jsf
/usr/share/joe/syntax/ada.jsf
/usr/share/joe/syntax/ant.jsf
/usr/share/joe/syntax/asm.jsf
/usr/share/joe/syntax/avr.jsf
/usr/share/joe/syntax/awk.jsf
/usr/share/joe/syntax/batch.jsf
/usr/share/joe/syntax/c.jsf
/usr/share/joe/syntax/clojure.jsf
/usr/share/joe/syntax/cobol.jsf
/usr/share/joe/syntax/coffee.jsf
/usr/share/joe/syntax/comment_todo.jsf
/usr/share/joe/syntax/conf.jsf
/usr/share/joe/syntax/context.jsf
/usr/share/joe/syntax/csh.jsf
/usr/share/joe/syntax/csharp.jsf
/usr/share/joe/syntax/css.jsf
/usr/share/joe/syntax/d.jsf
/usr/share/joe/syntax/debian.jsf
/usr/share/joe/syntax/diff.jsf
/usr/share/joe/syntax/dockerfile.jsf
/usr/share/joe/syntax/elixir.jsf
/usr/share/joe/syntax/erb.jsf
/usr/share/joe/syntax/erlang.jsf
/usr/share/joe/syntax/filename.jsf
/usr/share/joe/syntax/fortran.jsf
/usr/share/joe/syntax/git-commit.jsf
/usr/share/joe/syntax/go.jsf
/usr/share/joe/syntax/groovy.jsf
/usr/share/joe/syntax/haml.jsf
/usr/share/joe/syntax/haskell.jsf
/usr/share/joe/syntax/html.jsf
/usr/share/joe/syntax/htmlerb.jsf
/usr/share/joe/syntax/ini.jsf
/usr/share/joe/syntax/iptables.jsf
/usr/share/joe/syntax/java.jsf
/usr/share/joe/syntax/jcf.jsf
/usr/share/joe/syntax/joerc.jsf
/usr/share/joe/syntax/js.jsf
/usr/share/joe/syntax/jsf.jsf
/usr/share/joe/syntax/jsf_check.jsf
/usr/share/joe/syntax/json.jsf
/usr/share/joe/syntax/lisp.jsf
/usr/share/joe/syntax/lua.jsf
/usr/share/joe/syntax/m4.jsf
/usr/share/joe/syntax/mail.jsf
/usr/share/joe/syntax/mason.jsf
/usr/share/joe/syntax/matlab.jsf
/usr/share/joe/syntax/md.jsf
/usr/share/joe/syntax/ocaml.jsf
/usr/share/joe/syntax/pascal.jsf
/usr/share/joe/syntax/perl.jsf
/usr/share/joe/syntax/php.jsf
/usr/share/joe/syntax/powershell.jsf
/usr/share/joe/syntax/prolog.jsf
/usr/share/joe/syntax/properties.jsf
/usr/share/joe/syntax/ps.jsf
/usr/share/joe/syntax/puppet.jsf
/usr/share/joe/syntax/python.jsf
/usr/share/joe/syntax/r.jsf
/usr/share/joe/syntax/rexx.jsf
/usr/share/joe/syntax/ruby.jsf
/usr/share/joe/syntax/rust.jsf
/usr/share/joe/syntax/scala.jsf
/usr/share/joe/syntax/sed.jsf
/usr/share/joe/syntax/sh.jsf
/usr/share/joe/syntax/sieve.jsf
/usr/share/joe/syntax/skill.jsf
/usr/share/joe/syntax/sml.jsf
/usr/share/joe/syntax/spec.jsf
/usr/share/joe/syntax/sql.jsf
/usr/share/joe/syntax/swift.jsf
/usr/share/joe/syntax/tcl.jsf
/usr/share/joe/syntax/tex.jsf
/usr/share/joe/syntax/troff.jsf
/usr/share/joe/syntax/typescript.jsf
/usr/share/joe/syntax/verilog.jsf
/usr/share/joe/syntax/vhdl.jsf
/usr/share/joe/syntax/whitespace.jsf
/usr/share/joe/syntax/xml.jsf
/usr/share/joe/syntax/yaml.jsf
/usr/share/man/ru/man1/joe.1

%files doc
%defattr(-,root,root,-)
%doc /usr/share/doc/joe/*
%doc /usr/share/man/man1/*
