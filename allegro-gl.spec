Summary:	The Allegro game programming library GL backend
Summary(pl.UTF-8):   Wsparcie GL dla biblioteki do programowania gier Allegro
Name:		allegro-gl
Version:	0.2.4
Release:	1
License:	Giftware
Group:		Libraries
Source0:	http://dl.sourceforge.net/allegrogl/alleggl-%{version}.tar.bz2
# Source0-md5:	c73127de9bb118f45f4f7d29de739eae
URL:		http://allegrogl.sourceforge.net/
BuildRequires:	XFree86-devel
BuildRequires:	allegro-devel >= 4.0.0
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake
Requires:	allegro >= 4.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		specflags	-fomit-frame-pointer

%description
AllegroGL is a cross-platform GL backend for the Allegro library.

%description -l pl.UTF-8
AllegroGL jest przenośną biblioteką dodającą wsparcie GL
w aplikacjach używających biblioteki Allegro.

%package devel
Summary:	A game programming library - header files
Summary(pl.UTF-8):   Biblioteka do programowania gier - pliki nagłówkowe
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	allegro-devel >= 4.0.0

%description devel
AllegroGL is a cross-platform GL backend for the Allegro library.

This package contains header files neccessary for compiling
applications using AllegroGL library.

%description devel -l pl.UTF-8
AllegroGL jest przenośną biblioteką dodającą wsparcie GL
w aplikacjach używających biblioteki Allegro.

Ten pakiet zawiera pliki nagłówkowe niezbędne do kompilowania
aplikacji wykorzystujących bibliotekę AllegroGL.

%prep
%setup -q -n alleggl

%build
%{__aclocal}
%{__autoconf}
%configure \
	--enable-static \
%ifnarch %{ix86}
	--disable-asm \
	--disable-mmx \
	--disable-sse
%endif

%{__make} lib \
	CFLAGS="%{rpmcflags} -Wall -ffast-math"

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
