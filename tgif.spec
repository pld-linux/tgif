Summary:	tgif drawing package
Name:		tgif
Version:	4.1.7
Release:	1
Copyright:	custom
Group:		X11/Applications/Graphics
Group(pl):	X11/Aplikacje/Grafika
Source:		ftp://ftp.x.org/contrib/applications/tgif/%{name}-%{version}.tar.gz
URL:		http://bourbon.cs.umd.edu:8001/tgif/
Buildroot:	/tmp/%{name}-%{version}-root

%description
tgif is a drawing packages for X. It has better text and object support
than xfig, but is a little different to use.  

%prep
%setup -q

%build
xmkmf
make CDEBUGFLAGS="$RPM_OPT_FLAGS" tgif

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/usr/X11R6/lib/X11/app-defaults

make DESTDIR="$RPM_BUILD_ROOT" install
make DESTDIR="$RPM_BUILD_ROOT" install.man

mv $RPM_BUILD_ROOT/usr/X11R6/lib/X11/tgif/tgif.Xdefaults \
	$RPM_BUILD_ROOT/usr/X11R6/lib/X11/app-defaults/Tgif
gzip -9fn $RPM_BUILD_ROOT/usr/X11R6/man/man1/* \
	README HISTORY Copyright

%clean
#rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {README,HISTORY,Copyright}.gz
%attr(755,root,root) /usr/X11R6/bin/tgif
/usr/X11R6/lib/X11/tgif
/usr/X11R6/lib/X11/app-defaults/Tgif
/usr/X11R6/man/man1/*

%changelog
* Fri Apr  9 1999 Artur Frysiak <wiget@pld.org.pl>
  [4.1.4-1]
- added full decription of files permision
- gzipping doc
- using DESTDIR in install
- added Group(pl)

* Sat Dec 13 1997 Jan Prikryl <prikryl@acm.org>

Release 2: dependencies changed
           i386 RPM linked against libc.so.6

* Tue Aug 05 1997 Corey Minyard <minyard@acm.org>

Initial version
