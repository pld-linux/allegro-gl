Summary:	The Allegro game programming library GL backend
Summary(pl):	Wsparcie GL dla biblioteki do programowania gier Allegro
Name:		allegro-gl
Version:	0.2.2
Release:	1
License:	Giftware
Group:		Libraries
Source0:	http://dl.sourceforge.net/allegrogl/alleggl-%{version}.tar.gz
URL:		http://allegrogl.sourceforge.net/
BuildRequires:	allegro-devel
BuildRequires:	XFree86-devel
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake
Requires:	allegro
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
AllegroGL is a cross-platform GL backend for the Allegro library.

%description -l pl
AllegroGL jest przeno¶n± bibliotek± dodaj±c± wsparcie GL
w aplikacjach u¿ywaj±cych biblioteki Allegro.

%package devel
Summary:	A game programming library - header files
Summary(pl):	Biblioteka do programowania gier - pliki nag³ówkowe
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	allegro-devel

%description devel
AllegroGL is a cross-platform GL backend for the Allegro library.

This package contains header files neccessary for compiling
applications using AllegroGL library.

%description devel -l pl
AllegroGL jest przeno¶n± bibliotek± dodaj±c± wsparcie GL
w aplikacjach u¿ywaj±cych biblioteki Allegro.

Ten pakiet zawiera pliki nag³ówkowe niezbêdne do kompilowania
aplikacji wykorzystuj±cych bibliotekê AllegroGL.

%prep
%setup -q -n "alleggl"

%build
%{__aclocal}
%{__autoconf}
TARGET_ARCH="%{rpmcflags}" export TARGET_ARCH
# dbglib & proflib are compiled besides normlib, so it's ok to have them here
%configure \
	--enable-static \
%ifnarch %{ix86}
	--disable-asm \
	--disable-mmx \
	--disable-sse
%endif

%{__make} lib

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_libdir},%{_includedir}{,/allegrogl{,/GLext}}}

install include/*.h $RPM_BUILD_ROOT%{_includedir}
install include/allegrogl/*.h $RPM_BUILD_ROOT%{_includedir}/allegrogl
install include/allegrogl/GLext/*.h $RPM_BUILD_ROOT%{_includedir}/allegrogl/GLext
install lib/unix/libagl.so $RPM_BUILD_ROOT%{_libdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc readme.txt todo.txt bugs.txt
%attr(755,root,root) %{_libdir}/libagl.so

%files devel
%defattr(644,root,root,755)
%doc howto.txt
%{_includedir}/*
