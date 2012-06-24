Summary:	tgif drawing package
Summary(pl):	tgif - pakiet do tworzenia grafiki 2D
Summary(ja):	����Ū 2 ����������ưפˤ��� Xlib �˴�Ť��� X11 ���饤�����
Name:		tgif
Version:	4.1.40
Release:	1
License:	custom
Group:		X11/Applications/Graphics
Group(de):	X11/Applikationen/Grafik
Group(pl):	X11/Aplikacje/Grafika
Group(pt):	X11/Aplica��es/Gr�ficos
Source0:	ftp://bourbon.cs.umd.edu/pub/tgif/%{name}-%{version}.tar.gz
Source1:	%{name}.ap.ja
URL:		http://bourbon.cs.umd.edu:8001/tgif/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
tgif is a drawing packages for X. It has better text and object
support than xfig, but is a little different to use.

%description -l pl
tgif jest programem do rysowania w 2D pod X Window. Ma lepsze wsparcie
dla tekstu i obiekt�w ni� xfig, ale jest nieco trudniejszy w obs�udze.

%description -l ja
Tgif ������Ū�� 2 ����������ưפˤ��� Xlib �˴�Ť��� X11
���饤����ȤǤ�������γ��ع�¤������ν���֤δ�ñ�����
�򥵥ݡ��Ȥ��Ƥ��ޤ����ޤ� WWW �Υѥ��ѡ�������ե��å���
(�⤷���ϥϥ��ѡ������ȥ饯���㡼�ɡ�����ե��å���)���֥� �����Ǥ���

%prep
%setup -q

%build
rm -rf Tgif.tmpl
cp -f Tgif.tmpl-linux Tgif.tmpl
xmkmf
%{__make} MOREDEFINES="-DOVERTHESPOT -DUSE_XT_INITIALIZE -D_ENABLE_NLS \
	-DPRINT_CMD=\\\"lpr\\\" -DA4PAPER" TGIFDIR=%{_datadir}/tgif \
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

%{__make} DESTDIR="$RPM_BUILD_ROOT" TGIFDIR=%{_datadir}/tgif install install.man
install *.obj $RPM_BUILD_ROOT%{_datadir}/tgif

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
