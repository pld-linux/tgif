Summary:	tgif drawing package
Summary(pl):	tgif - pakiet do tworzenia grafiki 2D
Summary(ja):	ÂÐÏÃÅª 2 ¼¡¸µÉÁ²è¤òÍÆ°×¤Ë¤¹¤ë Xlib ¤Ë´ð¤Å¤¤¤¿ X11 ¥¯¥é¥¤¥¢¥ó¥È
Name:		tgif
Version:	4.1.44
Release:	1
License:	QPL
Group:		X11/Applications/Graphics
Source0:	ftp://bourbon.usc.edu/pub/tgif/%{name}-QPL-%{version}.tar.gz
# Source0-md5:	4818d79d36c460e24d14a390ade371e9
Source1:	%{name}.ap.ja
Patch0:		%{name}-po.patch
URL:		http://bourbon.usc.edu:8001/tgif/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdefsdir	/usr/X11R6/lib/X11/app-defaults

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

%build
rm -rf Tgif.tmpl
cp -f Tgif.tmpl-linux Tgif.tmpl
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
cd ..

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_appdefsdir}/ja/Tgif

%{__make} install install.man \
	DESTDIR=$RPM_BUILD_ROOT \
	BINDIR=%{_bindir} \
	MANDIR=%{_mandir}/man1 \
	TGIFDIR=%{_datadir}/tgif

install *.obj $RPM_BUILD_ROOT%{_datadir}/tgif

%{__make} -C po install \
	DESTDIR=$RPM_BUILD_ROOT

mv -f $RPM_BUILD_ROOT%{_datadir}/tgif/tgif.Xdefaults \
	$RPM_BUILD_ROOT%{_appdefsdir}/Tgif
install %{SOURCE1} $RPM_BUILD_ROOT%{_appdefsdir}/ja/Tgif

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README HISTORY Copyright
%attr(755,root,root) %{_bindir}/tgif
%{_datadir}/tgif
%{_mandir}/man1/*
%{_appdefsdir}/Tgif
%lang(ja) %{_appdefsdir}/ja/Tgif
