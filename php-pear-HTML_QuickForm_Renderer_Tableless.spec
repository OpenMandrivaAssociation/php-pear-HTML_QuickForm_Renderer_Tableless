%define		_class		HTML
%define		_subclass	QuickForm
%define		upstream_name	%{_class}_%{_subclass}_Renderer_Tableless

Name:		php-pear-%{upstream_name}
Version:	0.6.2
Release:	1
Summary:	Replacement for the default renderer
License:	PHP License
Group:		Development/PHP
URL:		http://pear.php.net/package/HTML_QuickForm_Renderer_Tableless
Source0:	http://download.pear.php.net/package/HTML_QuickForm_Renderer_Tableless-%{version}.tgz
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildArch:	noarch
BuildRequires:	php-pear

%description
Replacement for the default renderer that doesn't use table tags, and generates
fully valid XHTML output.

%prep
%setup -q -c
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%install

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean



%files
%defattr(-,root,root)
%doc %{upstream_name}-%{version}/docs/*
%{_datadir}/pear/%{_class}
%{_datadir}/pear/data/%{upstream_name}
%{_datadir}/pear/packages/%{upstream_name}.xml


%changelog
* Fri Dec 16 2011 Oden Eriksson <oeriksson@mandriva.com> 0.5.3-8mdv2012.0
+ Revision: 741999
- fix major breakage by careless packager

* Fri May 27 2011 Oden Eriksson <oeriksson@mandriva.com> 0.5.3-7
+ Revision: 679350
- mass rebuild

* Tue Dec 07 2010 Oden Eriksson <oeriksson@mandriva.com> 0.5.3-6mdv2011.0
+ Revision: 613676
- the mass rebuild of 2010.1 packages

* Sat Dec 12 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.5.3-5mdv2010.1
+ Revision: 477880
- spec cleanup
- use pear installer
- don't ship tests, even in documentation
- own all directories
- use rpm filetriggers starting from mandriva 2010.1

* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 0.5.3-4mdv2010.0
+ Revision: 441123
- rebuild

* Thu Jan 01 2009 Oden Eriksson <oeriksson@mandriva.com> 0.5.3-3mdv2009.1
+ Revision: 322117
- rebuild

* Thu Jul 17 2008 Oden Eriksson <oeriksson@mandriva.com> 0.5.3-2mdv2009.0
+ Revision: 236876
- rebuild

* Fri Dec 21 2007 Olivier Blin <blino@mandriva.org> 0.5.3-1mdv2008.1
+ Revision: 136407
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue Aug 21 2007 Oden Eriksson <oeriksson@mandriva.com> 0.5.3-1mdv2008.0
+ Revision: 68589
- Import php-pear-HTML_QuickForm_Renderer_Tableless



* Tue Aug 21 2007 Oden Eriksson <oeriksson@mandriva.com> 0.5.3-1mdv2008.0
- initial Mandriva package

