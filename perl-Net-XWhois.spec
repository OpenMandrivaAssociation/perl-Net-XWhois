%define name perl-Net-XWhois
%define real_name Net-XWhois
%define version 0.90

Name: %{name}
Version: %{version}
Summary: Extensible client framework for doing Whois queries and parsing server response
Release: %mkrel 6
License: GPL or Artistic
Group: Development/Perl
Source: %{real_name}-%{version}.tar.bz2
Url: http://www.cpan.org
BuildRequires:	perl-devel
BuildArch: noarch
Buildroot: %{_tmppath}/%{name}-root
Requires: perl >= 0:5.00503

%description
The Net::XWhois class provides an extensible client framework for
doing Whois queries and parsing server response. The class maintains
an array of whois servers and associated lists of top level domains
for transparently selecting servers appropriate for different queries.
Supports response caching and comes with a drop-in replacement for
the whois program. 

%prep
%setup -q -n %{real_name}-%{version}

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


