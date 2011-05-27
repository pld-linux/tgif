#
# TODO: - put icons to /usr/share/icons/hicolor instead of /usr/share/tgif/hicolor
#	- fix font opening
#
Summary:	tgif drawing package
Summary(ja.UTF-8):	対話的 2 次元描画を容易にする Xlib に基づいた X11 クライアント
Summary(pl.UTF-8):	tgif - pakiet do tworzenia grafiki 2D
Name:		tgif
Version:	4.2.3
Release:	0.1
License:	QPL
Group:		X11/Applications/Graphics
Source0:	ftp://bourbon.usc.edu/pub/tgif/%{name}-QPL-%{version}.tar.gz
# Source0-md5:	5a24337b944c693a514ffe7eb3ded4b6
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

%description -l pl.UTF-8
tgif jest programem do rysowania w 2D pod X Window. Ma lepsze wsparcie
dla tekstu i obiektów niż xfig, ale jest nieco trudniejszy w obsłudze.

%description -l ja.UTF-8
Tgif は対話的な 2 次元描画を容易にする Xlib に基づいた X11
クライアントです。描画の階層構造と描画の集合間の簡単な操作
をサポートしています。また WWW のパイパー・グラフィックス
(もしくはハイパー・ストラクチャード・グラフィックス)・ブラ ウザです。

%prep
%setup -q -n %{name}-QPL-%{version}
%patch0 -p1

cp -f Tgif.tmpl-linux Tgif.tmpl

%build
xmkmf
%{__make} tgif \
	CC="%{__cc}" \
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
%{_mandir}/man1/tgif.1*
%{_datadir}/X11/app-defaults/Tgif
%lang(ja) %{_datadir}/X11/ja/app-defaults/Tgif
