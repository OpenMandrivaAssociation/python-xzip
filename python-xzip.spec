%define oname   xzip
%define name    python-%oname
%define version 0.1
%define release 10


Summary:       Sequence index and item ranges for python
Name:          %{name}
Version:       %{version}
Release:       %{release}
Source0:       %{oname}.py
License:       LGPL
Group:         Development/Python
BuildRoot:     %{_tmppath}/%{name}-buildroot
Url:           https://www.python.org/peps/pep-0212.html
BuildRequires: python
BuildArch:     noarch

%description
This is a python module providing lazy versions of the built-in zip,
map, and filter functions.

%install
rm -rf $RPM_BUILD_ROOT
install -m644 -D %SOURCE0 $RPM_BUILD_ROOT/%py_puresitedir/%{oname}.py
cd $RPM_BUILD_ROOT%py_puresitedir
python -c "import %{oname}"

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%py_puresitedir/%{oname}.py



%changelog
* Wed Nov 17 2010 Funda Wang <fwang@mandriva.org> 0.1-9mdv2011.0
+ Revision: 598145
- rebuild for py2.7

* Tue Sep 08 2009 Thierry Vignaud <tv@mandriva.org> 0.1-9mdv2010.0
+ Revision: 433750
- rebuild

* Mon Sep 07 2009 Thierry Vignaud <tv@mandriva.org> 0.1-8mdv2010.0
+ Revision: 432086
- rebuild

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 0.1-7mdv2009.0
+ Revision: 242467
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Thu Aug 23 2007 Thierry Vignaud <tv@mandriva.org> 0.1-5mdv2008.0
+ Revision: 69371
- use %%mkrel


* Tue Dec 07 2004 Michael Scherer <misc@mandrake.org> 0.1-4mdk
- Really Rebuild for new python

* Sun Dec 05 2004 Michael Scherer <misc@mandrake.org> 0.1-3mdk
- Rebuild for new python

* Sat Aug 09 2003 Austin Acton <aacton@yorku.ca> 0.1-2mdk
- python 2.3

* Wed Jul 09 2003 Austin Acton <aacton@yorku.ca> 0.1-1mdk
- from andi payn <payn@myrealbox.com> :
  - new version

