Summary:	tgif drawing package
Summary(pl):	tgif - pakiet do tworzenia grafiki 2D
Summary(ja):	対話的 2 次元描画を容易にする Xlib に基づいた X11 クライアント
Name:		tgif
Version:	4.1.42
Release:	4
License:	QPL
Group:		X11/Applications/Graphics
Source0:	ftp://bourbon.usc.edu/pub/tgif/%{name}-QPL-%{version}.tar.gz
# Source0-md5:	83b1cd01b1570fbf71ea5994af87f42e
Source1:	%{name}.ap.ja
Patch0:		%{name}-po.patch
URL:		http://bourbon.usc.edu:8001/tgif/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
tgif is a drawing packages for X. It has better text and object
support than xfig, but is a little different to use.

%description -l pl
tgif jest programem do rysowania w 2D pod X Window. Ma lepsze wsparcie
dla tekstu i obiekt�w ni� xfig, ale jest nieco trudniejszy w obs�udze.

%description -l ja
Tgif は対話的な 2 次元描画を容易にする Xlib に基づいた X11
クライアントです。描画の階層構造と描画の集合間の簡単な操作
をサポートしています。また WWW のパイパー・グラフィックス
(もしくはハイパー・ストラクチャード・グラフィックス)・ブラ ウザです。

%prep
%setup -q -n %{name}-QPL-%{version}
%patch0 -p1

%build
rm -rf Tgif.tmpl
cp -f Tgif.tmpl-linux Tgif.tmpl
xmkmf
%{__make} tgif \
	MOREDEFINES="-DOVERTHESPOT -DUSE_XT_INITIALIZE -D_ENABLE_NLS \
	-DPRINT_CMD=\\\"lpr\\\" -DA4PAPER" TGIFDIR="%{_datadir}/tgif" \
	LOCAL_LIBRARIES="-lXmu -lXt -lX11" \
	CDEBUGFLAGS="%{rpmcflags}"

cd po
xmkmf -a
%{__make} depend
%{__make} all
cd ..

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_libdir}/X11/app-defaults/ja

%{__make} DESTDIR="$RPM_BUILD_ROOT" TGIFDIR=%{_datadir}/tgif install install.man
install *.obj $RPM_BUILD_ROOT%{_datadir}/tgif

%{__make} -C po DESTDIR="$RPM_BUILD_ROOT" install

mv -f $RPM_BUILD_ROOT%{_datadir}/tgif/tgif.Xdefaults \
	$RPM_BUILD_ROOT%{_libdir}/X11/app-defaults/Tgif
install %{SOURCE1} $RPM_BUILD_ROOT%{_libdir}/X11/app-defaults/ja/Tgif

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README HISTORY Copyright
%attr(755,root,root) %{_bindir}/tgif
%{_datadir}/tgif
%{_mandir}/man1/*
%{_libdir}/X11/app-defaults/Tgif
%lang(ja) %{_libdir}/X11/app-defaults/ja/Tgif
