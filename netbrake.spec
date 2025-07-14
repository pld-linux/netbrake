Summary:	Netbrake - an utility to limit the bandwidth used by a process
Summary(pl.UTF-8):	Netbrake - narzędzie do ograniczania łącza używanego przez proces
Name:		netbrake
Version:	0.2
Release:	2
# netbrake app contains GPLed antigetopt.c, so it's whole GPLed
License:	GPL (application), BSD-like (libnetbrake)
Group:		Applications/Networking
Source0:	http://www.hping.org/netbrake/%{name}-%{version}.tar.gz
# Source0-md5:	42f61481cdb910bddd1105d48367bdd2
Patch0:		%{name}-make.patch
Patch1:		%{name}-types.patch
URL:		http://www.hping.org/netbrake/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Netbrake is an utility to limit the bandwidth used by a process. It
does not require to modify the kernel, nor to be root in order to
work. It is useful when you need to download a very big file from a
fast server to avoid a network congestion that will result in a too
slow web/irc/... experience. I use it mostly to download big files
(like the kernel source code) with wget.

Netbrake also implements a very simple HTTP filesystem extension, so
you can use the standard text utils against some URL.

%description -l pl.UTF-8
Netbrake jest narzędziem do ograniczania przepustowości łącza
używanego przez proces. Nie wymaga modyfikacji jądra, działa na
zwykłym koncie, jest używane głównie wtedy, gdy chcemy ściągnąć duże
pliki np. za pomocą wgeta czy lynksa.

Netbrake ma także zaimplementowane proste rozszerzenie systemu
plików o HTTP, dzięki czemu można używać standardowych narzędzi
tekstowych na URL-ach.

%prep
%setup -q -n %{name}
%patch -P0 -p0
%patch -P1 -p1

%build
# not autoconf configure
LIBPATH="%{_libdir}" \
./configure

%{__make} \
	CFLAGS="%{rpmcflags}" \
	CC="%{__cc}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir},%{_bindir}}

%{__make} install \
	BINPATH=$RPM_BUILD_ROOT%{_bindir} \
	LIBPATH=$RPM_BUILD_ROOT%{_libdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post    -p /sbin/ldconfig
%postun  -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS LICENSE THANKS README TODO
%attr(755,root,root) %{_bindir}/netbrake
%attr(755,root,root) %{_libdir}/libnetbrake.so.*.*
