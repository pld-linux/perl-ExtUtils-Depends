#
# Conditional build:
%bcond_without tests 	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	ExtUtils
%define	pnam	Depends
Summary:	ExtUtils::Depends - Easily build XS extensions
Summary(pl):	ExtUtils::Depends - ³atwe budowanie rozszerzeñ XS
Name:		perl-%{pdir}-%{pnam}
Version:	0.201
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://dl.sourceforge.net/gtk2-perl/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	16e9388eed0a593b2f98f3551c8c462d
URL:		http://gtk2-perl.sf.net/
BuildRequires:	perl-devel >= 5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module tries to make it easy to build Perl extensions that use
functions and typemaps provided by other Perl extensions.

%description -l pl
Ten modu³ próbuje u³atwiæ budowanie perlowych rozszerzeñ u¿ywaj±cych
funkcji i map typów udostêpnianych przez inne rozszerzenia Perla.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make} \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/ExtUtils/Depends.pm
%{_mandir}/man3/*
