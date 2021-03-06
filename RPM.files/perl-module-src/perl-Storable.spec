Summary: Storable Perl module
Name: perl-Storable
Version: 2.16
Release: 3
Packager: mailscanner@ecs.soton.ac.uk
License: GPL or Artistic
Group: Development/Libraries
URL: http://search.cpan.org/dist/Storable/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch
#BuildRequires: perl >= 0:5.00503
Source0: Storable-2.16.tar.gz

%description
Storable Perl module

%description
Storable Perl module
%prep
%setup -q -n Storable-%{version} 1

%build
CFLAGS="$RPM_OPT_FLAGS" perl Makefile.PL INSTALLDIRS="vendor"
make
make test

%clean
rm -rf $RPM_BUILD_ROOT
%install

rm -rf $RPM_BUILD_ROOT
eval `perl '-V:installarchlib'`
mkdir -p $RPM_BUILD_ROOT/$installarchlib
make pure_install DESTDIR=$RPM_BUILD_ROOT

### Clean up buildroot
find $RPM_BUILD_ROOT -name .packlist -exec %{__rm} {} \;

[ -x /usr/lib/rpm/brp-compress ] && /usr/lib/rpm/brp-compress

find $RPM_BUILD_ROOT/usr -type f -print | \
	sed "s@^$RPM_BUILD_ROOT@@g" | \
	grep -v perllocal.pod | \
	grep -v "\.gz" | \
	grep -v "\.packlist" > Storable-%{version}-filelist
if [ "$(cat Storable-%{version}-filelist)X" = "X" ] ; then
    echo "ERROR: EMPTY FILE LIST"
    exit 1
fi

%files -f Storable-%{version}-filelist
%defattr(-,root,root)

%changelog
* Sat Apr 11 2009 Julian Field <mailscanner@ecs.soton.ac.uk>
- Spec file changed to match Dag's tricks with vendorlib install
* Sun Oct 06 2002 Julian Field <mailscanner@ecs.soton.ac.uk>
- Specfile autogenerated

