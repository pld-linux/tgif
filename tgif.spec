Summary:	tgif drawing package
Name:		tgif
Version:	4.1.3
Release:	1
Copyright:	custom
Group:		X11/Applications/Graphics
Source:		ftp://ftp.x.org/contrib/applications/tgif/%{name}-%{version}.tar.gz
Buuldroot:	/tmp/%{name}-%{version}-root
%description
tgif is a drawing packages for X. It has better text and object support
than xfig, but is a little different to use.  

%changelog

* Sat Dec 13 1997 Jan Prikryl <prikryl@acm.org>

Release 2: dependencies changed
           i386 RPM linked against libc.so.6

* Tue Aug 05 1997 Corey Minyard <minyard@acm.org>

Initial version

%prep
%setup -n tgif-3.0-p13

%build
xmkmf
make CDEBUGFLAGS=-O2

%install
make install
make install.man

%files
%doc README
/usr/X11R6/bin/tgif
/usr/X11R6/bin/prtgif
/usr/X11R6/lib/X11/tgif
/usr/X11R6/man/man1/tgif.1x
/usr/X11R6/man/man1/prtgif.1x
