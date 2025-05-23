#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
# autospec version: v21
# autospec commit: 94c6be0
#
Name     : perl-POD2-Base
Version  : 0.043
Release  : 31
URL      : https://cpan.metacpan.org/authors/id/F/FE/FERREIRA/POD2-Base-0.043.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/F/FE/FERREIRA/POD2-Base-0.043.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libp/libpod2-base-perl/libpod2-base-perl_0.043-2.debian.tar.xz
Summary  : Base module for translations of Perl documentation
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-POD2-Base-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
NAME
POD2::Base - Base module for translations of Perl documentation
SYNOPSIS
use POD2::Base;
$pod2 = POD2::Base->new({ lang => 'EO' });

%package dev
Summary: dev components for the perl-POD2-Base package.
Group: Development
Provides: perl-POD2-Base-devel = %{version}-%{release}
Requires: perl-POD2-Base = %{version}-%{release}

%description dev
dev components for the perl-POD2-Base package.


%package perl
Summary: perl components for the perl-POD2-Base package.
Group: Default
Requires: perl-POD2-Base = %{version}-%{release}

%description perl
perl components for the perl-POD2-Base package.


%prep
%setup -q -n POD2-Base-0.043
cd %{_builddir}
tar xf %{_sourcedir}/libpod2-base-perl_0.043-2.debian.tar.xz
cd %{_builddir}/POD2-Base-0.043
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/POD2-Base-0.043/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/POD2::Base.3
/usr/share/man/man3/POD2::PT::POD2::Base.3

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
