%define upstream_name    Net-XWhois
%define upstream_version 0.90

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	Extensible client framework for doing Whois queries and parsing server response
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Net/%{upstream_name}-%{upstream_version}.tar.bz2

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
%setup -q -n %{upstream_name}-%{upstream_version}

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

%changelog
* Mon Aug 03 2009 Jérôme Quelin <jquelin@mandriva.org> 0.900.0-1mdv2010.0
+ Revision: 407946
- rebuild using %%perl_convert_version

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 0.90-7mdv2009.0
+ Revision: 258138
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.90-6mdv2009.0
+ Revision: 246209
- rebuild

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 0.90-4mdv2008.1
+ Revision: 140694
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Sun Jan 14 2007 Olivier Thauvin <nanardon@mandriva.org> 0.90-4mdv2007.0
+ Revision: 108469
- rebuild

  + Guillaume Rousse <guillomovitch@mandriva.org>
    - Import perl-Net-XWhois

