Summary:	The Allegro game programming library GL backend
Summary(pl.UTF-8):	Wsparcie GL dla biblioteki do programowania gier Allegro
Name:		allegro-gl
Version:	0.4.3
Release:	1
License:	GPL v2 or zlib
Group:		Libraries
Source0:	http://dl.sourceforge.net/allegrogl/alleggl-%{version}.tar.bz2
# Source0-md5:	de84c6ab982499501940854893ea0dbd
Patch0:		%{name}-mouse.patch
Patch1:		%{name}-link.patch
Patch2:		%{name}-libpthread.patch
URL:		http://allegrogl.sourceforge.net/
BuildRequires:	OpenGL-GLU-devel
BuildRequires:	allegro-devel >= 4.3.1
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake
Requires:	allegro >= 4.3.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		specflags	-fomit-frame-pointer

%description
AllegroGL is a cross-platform GL backend for the Allegro library.

%description -l pl.UTF-8
AllegroGL jest przenośną biblioteką dodającą wsparcie GL
w aplikacjach używających biblioteki Allegro.

%package devel
Summary:	A game programming library - header files
Summary(pl.UTF-8):	Biblioteka do programowania gier - pliki nagłówkowe
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	allegro-devel >= 4.3.1

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
%patch0 -p1
%patch1 -p1
%patch2 -p1

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
install -d $RPM_BUILD_ROOT{%{_libdir},%{_includedir}/allegrogl/GLext}

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
%doc bugs.txt readme.txt todo.txt zlib.txt
%attr(755,root,root) %{_libdir}/libagl.so

%files devel
%defattr(644,root,root,755)
%doc howto.txt
%{_includedir}/alleggl*.h
%{_includedir}/allegrogl
