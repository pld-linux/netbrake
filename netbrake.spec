Summary:	Netbrake is an utility to limit the bandwidth used by a process
Summary(pl):	Netbrake jest narzêdziem do ograniczania ³±cza u¿ywanego przez proces
Name:		netbrake
Version:	0.1
Release:	1
License:	GPL
Group:		Applications/Networking
Source0:	http://www.hping.org/netbrake/%{name}-%{version}.tar.gz
Patch0:		ftp://ftp.linuxpl.com/pub/cvs/compil.patch
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
you can use the standard text utils against some URL

%description -l pl
Netbrake jest narzêdziem do ograniczania przepustowosci ³acza
u¿ywanego przez proces. Nie wymaga modyfikacji j±dra, dzia³a na
zwyk³ym koncie, jest u¿ywany g³ównie wtedy, gdy chcemy ¶ci±gn±æ du¿e
pliki np za. pomoc± wgeta czy lynksa.

%prep
%setup -q -n %{name}_%{version}
%patch0 -p0

%build
%configure

%{__make} CFLAGS="%{rpmcflags} "

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir},%{_bindir}}

%{__make} install \
	      LIBPATH=$RPM_BUILD_ROOT%{_libdir} BINPATH=$RPM_BUILD_ROOT%{_bindir}

gzip -9nf AUTHORS LICENSE THANKS README TODO

%post    -p /sbin/ldconfig
%postun  -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/netbrake
%attr(755,root,root) %{_libdir}/libnetbrake.so.*
