#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-POD2-Base
Version  : 0.0301
Release  : 2
URL      : https://cpan.metacpan.org/authors/id/F/FE/FERREIRA/POD2-Base-0.0301.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/F/FE/FERREIRA/POD2-Base-0.0301.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libp/libpod2-base-perl/libpod2-base-perl_0.043-2.debian.tar.xz
Summary  : Base module for translations of Perl documentation
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-POD2-Base-man

%description
NAME
POD2::Base - Base module for translations of Perl documentation
SYNOPSIS
use POD2::Base;
$pod2 = POD2::Base->new({ lang => 'EO' });

%package man
Summary: man components for the perl-POD2-Base package.
Group: Default

%description man
man components for the perl-POD2-Base package.


%prep
tar -xf %{SOURCE1}
cd ..
%setup -q -n POD2-Base-0.0301
mkdir -p %{_topdir}/BUILD/POD2-Base-0.0301/deblicense/
mv %{_topdir}/BUILD/debian/* %{_topdir}/BUILD/POD2-Base-0.0301/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot}
else
./Build install --installdirs=site --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/site_perl/5.26.1/POD2/Base.pm
/usr/lib/perl5/site_perl/5.26.1/POD2/Base.pod

%files man
%defattr(-,root,root,-)
/usr/share/man/man3/POD2::Base.3
