#
# Conditional build:
%bcond_with	tests		# perform "make test" (tests 23, 25-30 from more.t fail in
 				# February - except leap years)
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Date
%define		pnam	Tie
Summary:	Date::Tie - ISO dates made easy
Summary(pl):	Date::Tie - u³atwienia do dat ISO
Name:		perl-Date-Tie
Version:	0.17
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	4039e413eb514047eb1d2e8d84304091
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Date::Tie is an attempt to simplify date operations syntax.

It works with calendar dates (year-month-day), ordinal dates
(year-day), week dates (year-week-day), times (hour:minute:second),
decimal fractions (decimal hours, decimal minutes and decimal
seconds), and time-zones.

%description -l pl
Date::Tie to próba uproszczenia sk³adni operacji na datach.

Modu³ dzia³a z datami kalendarzowymi (rok-miesi±c-dzieñ), datami
porz±dkowymi (rok-dzieñ), datami tygodniowymi (rok-tydzieñ-dzieñ),
czasem (godzina:minuta:sekunda), u³amkami dziesiêtnymi (dziesiêtne
godziny, dziesiêtne minuty i dziesiêtne sekundy) i strefami czasowymi.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/%{pdir}/*.pm
%{_mandir}/man3/*
