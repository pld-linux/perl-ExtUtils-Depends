#
# Conditional build:
%bcond_without	tests 	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	ExtUtils
%define	pnam	Depends
Summary:	ExtUtils::Depends - easily build XS extensions
Summary(pl):	ExtUtils::Depends - �atwe budowanie rozszerze� XS
Name:		perl-ExtUtils-Depends
Version:	0.202
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://dl.sourceforge.net/gtk2-perl/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	28e432f68ccdeff2a8e69a745b84584f
URL:		http://gtk2-perl.sf.net/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module tries to make it easy to build Perl extensions that use
functions and typemaps provided by other Perl extensions.

%description -l pl
Ten modu� pr�buje u�atwi� budowanie perlowych rozszerze� u�ywaj�cych
funkcji i map typ�w udost�pnianych przez inne rozszerzenia Perla.

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
