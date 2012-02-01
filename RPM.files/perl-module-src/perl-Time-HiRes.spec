Summary: Time-HiRes Perl module
Name: perl-Time-HiRes
Version: 1.9707
Release: 3
Packager: mailscanner@ecs.soton.ac.uk
License: GPL or Artistic
Group: Development/Libraries
URL: http://search.cpan.org/dist/Time-HiRes/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch
#BuildRequires: perl >= 0:5.00503
Source0: Time-HiRes-1.9707.tar.gz

%description
Time-HiRes Perl module

%description
Time-HiRes Perl module
%prep
%setup -q -n Time-HiRes-%{version} 1

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
	grep -v "\.packlist" > Time-HiRes-%{version}-filelist
if [ "$(cat Time-HiRes-%{version}-filelist)X" = "X" ] ; then
    echo "ERROR: EMPTY FILE LIST"
    exit 1
fi

%files -f Time-HiRes-%{version}-filelist
%defattr(-,root,root)

%changelog
* Sat Apr 11 2009 Julian Field <mailscanner@ecs.soton.ac.uk>
- Spec file changed to match Dag's tricks with vendorlib install
* Sun Oct 06 2002 Julian Field <mailscanner@ecs.soton.ac.uk>
- Specfile autogenerated
