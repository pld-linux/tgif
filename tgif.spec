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
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_libdir}/X11/app-defaults

%{__make} DESTDIR="$RPM_BUILD_ROOT" install

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
