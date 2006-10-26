Summary:	tgif drawing package
Summary(pl):	tgif - pakiet do tworzenia grafiki 2D
Summary(ja):	ÂÐÏÃÅª 2 ¼¡¸µÉÁ²è¤òÍÆ°×¤Ë¤¹¤ë Xlib ¤Ë´ð¤Å¤¤¤¿ X11 ¥¯¥é¥¤¥¢¥ó¥È
Name:		tgif
Version:	4.1.45
Release:	1
License:	QPL
Group:		X11/Applications/Graphics
Source0:	ftp://bourbon.usc.edu/pub/tgif/%{name}-QPL-%{version}.tar.gz
# Source0-md5:	5c1eba8291385c630b8099fa9b042455
Source1:	%{name}.ap.ja
Patch0:		%{name}-po.patch
URL:		http://bourbon.usc.edu/tgif/
BuildRequires:	xorg-cf-files
BuildRequires:	xorg-lib-libXmu-devel
BuildRequires:	xorg-util-imake
Requires:	xorg-lib-libXt >= 1.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
tgif is a drawing packages for X. It has better text and object
support than xfig, but is a little different to use.

%description -l pl
tgif jest programem do rysowania w 2D pod X Window. Ma lepsze wsparcie
dla tekstu i obiektów ni¿ xfig, ale jest nieco trudniejszy w obs³udze.

%description -l ja
Tgif ¤ÏÂÐÏÃÅª¤Ê 2 ¼¡¸µÉÁ²è¤òÍÆ°×¤Ë¤¹¤ë Xlib ¤Ë´ð¤Å¤¤¤¿ X11
¥¯¥é¥¤¥¢¥ó¥È¤Ç¤¹¡£ÉÁ²è¤Î³¬ÁØ¹½Â¤¤ÈÉÁ²è¤Î½¸¹ç´Ö¤Î´ÊÃ±¤ÊÁàºî
¤ò¥µ¥Ý¡¼¥È¤·¤Æ¤¤¤Þ¤¹¡£¤Þ¤¿ WWW ¤Î¥Ñ¥¤¥Ñ¡¼¡¦¥°¥é¥Õ¥£¥Ã¥¯¥¹
(¤â¤·¤¯¤Ï¥Ï¥¤¥Ñ¡¼¡¦¥¹¥È¥é¥¯¥Á¥ã¡¼¥É¡¦¥°¥é¥Õ¥£¥Ã¥¯¥¹)¡¦¥Ö¥é ¥¦¥¶¤Ç¤¹¡£

%prep
%setup -q -n %{name}-QPL-%{version}
%patch0 -p1

cp -f Tgif.tmpl-linux Tgif.tmpl

%build
xmkmf
%{__make} tgif \
	MOREDEFINES="-DOVERTHESPOT -DUSE_XT_INITIALIZE -D_ENABLE_NLS \
	-DPRINT_CMD=\\\"lpr\\\" -DA4PAPER" \
	TGIFDIR="%{_datadir}/tgif" \
	LOCAL_LIBRARIES="-lXmu -lXt -lX11" \
	CDEBUGFLAGS="%{rpmcflags}"

cd po
xmkmf -a
%{__make} depend
%{__make} all

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/X11{,/ja}/app-defaults

%{__make} install install.man \
	DESTDIR=$RPM_BUILD_ROOT \
	BINDIR=%{_bindir} \
	MANDIR=%{_mandir}/man1 \
	TGIFDIR=%{_datadir}/tgif

install *.obj $RPM_BUILD_ROOT%{_datadir}/tgif

%{__make} -C po install \
	DESTDIR=$RPM_BUILD_ROOT

mv -f $RPM_BUILD_ROOT%{_datadir}/tgif/tgif.Xdefaults \
	$RPM_BUILD_ROOT%{_datadir}/X11/app-defaults/Tgif
install %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/X11/ja/app-defaults/Tgif

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README HISTORY Copyright
%attr(755,root,root) %{_bindir}/tgif
%{_datadir}/tgif
%{_mandir}/man1/*
%{_datadir}/X11/app-defaults/Tgif
%lang(ja) %{_datadir}/X11/ja/app-defaults/Tgif
