#
# Conditional build:
%bcond_without	tests 	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	ExtUtils
%define		pnam	Depends
Summary:	ExtUtils::Depends - easily build XS extensions that depend on XS extensions
Summary(pl.UTF-8):	ExtUtils::Depends - łatwe budowanie rozszerzeń XS zależących od innych rozszerzeń XS
Name:		perl-ExtUtils-Depends
Version:	0.405
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/ExtUtils/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	caefbca2f173d0cea3f5ac26b6c08a2c
URL:		http://search.cpan.org/dist/ExtUtils-Depends/
BuildRequires:	perl-devel >= 1:5.8.0
%if %{with tests}
BuildRequires:	perl-Test-Number-Delta >= 1.0
BuildRequires:	perl-Test-Simple
%endif
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module tries to make it easy to build Perl extensions that use
functions and typemaps provided by other Perl extensions.

%description -l pl.UTF-8
Ten moduł próbuje ułatwić budowanie perlowych rozszerzeń używających
funkcji i map typów udostępnianych przez inne rozszerzenia Perla.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make} \
	CC="%{__cc}" \
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
%doc Changes
%{perl_vendorlib}/ExtUtils/Depends.pm
%{_mandir}/man3/ExtUtils::Depends.3pm*
