Summary:	tgif drawing package
Summary(pl):	tgif - pakiet do tworzenia grafiki 2D
Name:		tgif
Version:	4.1.16
Release:	1
Copyright:	custom
Group:		X11/Applications/Graphics
Group(pl):	X11/Aplikacje/Grafika
Source:		ftp://bourbon.cs.umd.edu/pub/tgif/%{name}-%{version}.tar.gz
URL:		http://bourbon.cs.umd.edu:8001/tgif/
Buildroot:	/tmp/%{name}-%{version}-root

%define _prefix /usr/X11R6

%description
tgif is a drawing packages for X. It has better text and object support
than xfig, but is a little different to use.  

%prep
%setup -q

%build
autoconf
CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-s" \
./configure \
	--prefix=%{_prefix}
make

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_libdir}/X11/app-defaults

make DESTDIR="$RPM_BUILD_ROOT" install

mv $RPM_BUILD_ROOT%{_datadir}/tgif/tgif.Xdefaults \
	$RPM_BUILD_ROOT%{_libdir}/X11/app-defaults/Tgif
gzip -9fn $RPM_BUILD_ROOT%{_mandir}/man1/* \
	README HISTORY Copyright

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc {README,HISTORY,Copyright}.gz
%attr(755,root,root) %{_bindir}/tgif
%{_datadir}/tgif
%{_mandir}/man1/*

%{_libdir}/X11/app-defaults/Tgif

%changelog
* Tue Jun  8 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [4.1.15-1]
- added more rpm macros,
- package can be now builded on systems FFHS 2.0 compliant.

* Thu Apr 15 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [4.1.4-1]
- moved data files for tgif to /usr/X11R6/share/tgif,
- enabled NLS support (added ja .mo file).

* Fri Apr  9 1999 Artur Frysiak <wiget@pld.org.pl>
- added full decription of files permision
- gzipping doc
- using DESTDIR in install
- added Group(pl)

* Sat Dec 13 1997 Jan Prikryl <prikryl@acm.org>
Release 2: dependencies changed
           i386 RPM linked against libc.so.6

* Tue Aug 05 1997 Corey Minyard <minyard@acm.org>
Initial version
