%define upstream_name    Net-XWhois
%define upstream_version 0.90

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Extensible client framework for doing Whois queries and parsing server response
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Net/%{upstream_name}-%{upstream_version}.tar.bz2

BuildArch: noarch
Buildroot: %{_tmppath}/%{name}-%{version}-%{release}

%description
The Net::XWhois class provides an extensible client framework for
doing Whois queries and parsing server response. The class maintains
an array of whois servers and associated lists of top level domains
for transparently selecting servers appropriate for different queries.
Supports response caching and comes with a drop-in replacement for
the whois program. 

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%clean 
rm -rf $RPM_BUILD_ROOT

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%files
%defattr(-,root,root)
%doc TODO ARTISTIC contribs/*
%{perl_vendorlib}/Net/*
%{_mandir}/*/*
