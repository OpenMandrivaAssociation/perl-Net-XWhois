%define upstream_name    Net-XWhois
%define upstream_version 0.90
Name:		perl-%{upstream_name}
Version:	0.90
Release:	1

Summary:	Extensible client framework for doing Whois queries and parsing server response
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/Net-XWhois
Source0:	https://cpan.metacpan.org/authors/id/V/VI/VIPUL/Net-XWhois-0.90.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildArch:	noarch

%description
The Net::XWhois class provides an extensible client framework for
doing Whois queries and parsing server response. The class maintains
an array of whois servers and associated lists of top level domains
for transparently selecting servers appropriate for different queries.
Supports response caching and comes with a drop-in replacement for
the whois program. 

%prep
%setup -q -n %{upstream_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc TODO ARTISTIC contribs/*
%{perl_vendorlib}/Net/*
%{_mandir}/*/*

