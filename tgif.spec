Summary:	tgif drawing package
Summary(pl):	tgif - pakiet do tworzenia grafiki 2D
Summary(ja): 	対話的 2 次元描画を容易にする Xlib に基づいた X11 クライアント
Name:		tgif
Version:	4.1.40
Release:	1
Copyright:	custom
Group:		X11/Applications/Graphics
Group(pl):	X11/Aplikacje/Grafika
Source0:	ftp://bourbon.cs.umd.edu/pub/tgif/%{name}-%{version}.tar.gz
Source1:	tgif.ap.ja
URL:		http://bourbon.cs.umd.edu:8001/tgif/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
tgif is a drawing packages for X. It has better text and object support
than xfig, but is a little different to use.  

%description -l pl
tgif jest programem do rysowania w 2D pod X Window. Ma lepsze wsparcie
dla tekstu i obiekt�w ni� xfig, ale jest nieco trudniejszy w obs�udze.

%description -l ja
Tgif は対話的な 2 次元描画を容易にする Xlib に基づいた X11
クライアントです。描画の階層構造と描画の集合間の簡単な操作
をサポートしています。また WWW のパイパー・グラフィックス
(もしくはハイパー・ストラクチャード・グラフィックス)・ブラ
ウザです。

%prep
%setup -q

%build
rm -rf Tgif.tmpl
cp Tgif.tmpl-linux Tgif.tmpl
xmkmf
%{__make} MOREDEFINES="-DOVERTHESPOT -DUSE_XT_INITIALIZE -D_ENABLE_NLS \
	-DPRINT_CMD=\\\"lpr\\\" -DA4PAPER" TGIFDIR=/usr/X11R6/share/tgif \
	LOCAL_LIBRARIES="-lXmu -lXt -lX11" tgif

cd po
xmkmf 
%{__make} Makefile
%{__make} Makefiles
%{__make} depend
%{__make} all
cd ..

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_libdir}/X11/{,ja/}app-defaults

%{__make} DESTDIR="$RPM_BUILD_ROOT" TGIFDIR=/usr/X11R6/share/tgif install install.man
install -m 644 *.obj $RPM_BUILD_ROOT%{_datadir}/tgif

%{__make} -C po DESTDIR="$RPM_BUILD_ROOT" install

mv -f $RPM_BUILD_ROOT%{_datadir}/tgif/tgif.Xdefaults \
	$RPM_BUILD_ROOT%{_libdir}/X11/app-defaults/Tgif
install %{SOURCE1} $RPM_BUILD_ROOT%{_libdir}/X11/ja/app-defaults/Tgif 
gzip -9fn README HISTORY Copyright

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
