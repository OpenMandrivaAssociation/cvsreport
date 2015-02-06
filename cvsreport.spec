%define name    cvsreport
%define version 0.3.5
%define release 9

Name:       %{name}
Version:    %{version}
Release:    %{release}
Summary:    Produce CVS activity reports
License:    GPL
Group:      System/Servers
URL:        http://home.gna.org/cvsreport/
Source:     http://download.gna.org/cvsreport/cvsreport.pkg/0.3.5/%{name}-%{version}.tar.bz2
BuildArch:  noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}

%description
CVSreport produces text or enhanced HTML activity reports from a local or
remote CVS repository. It can be used to extract activity information from any
time span, or to automatically generate reports and store/send them on commit
events.

CVSreport can extract changesets from a CVS repository history. A changeset is
a set of commit operations (addition, removal, modification) which happen along
a single invocation of the cvs commit command. Used from client side, it
produces a report starting from an arbitrary date from a simple working copy.
On the server side, it can automatically generate reports and mail them upon
commit.

%prep
%setup -q
chmod 644 ChangeLog

%build

%install
rm -rf %{buildroot}
%makeinstall_std PREFIX=%{_prefix}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc COPYING ChangeLog TODO README NEWS examples test
%{_bindir}/%{name}
%{_mandir}/man1/*



%changelog
* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 0.3.5-8mdv2011.0
+ Revision: 617485
- the mass rebuild of 2010.0 packages

* Wed Sep 02 2009 Thierry Vignaud <tv@mandriva.org> 0.3.5-7mdv2010.0
+ Revision: 425688
- rebuild

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 0.3.5-6mdv2009.0
+ Revision: 243838
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Tue Dec 18 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.3.5-4mdv2008.1
+ Revision: 132418
- rebuild

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - import cvsreport


* Tue Aug 29 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.3.5-3mdv2007.0
- Rebuild

* Mon Mar 27 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.3.5-2mdk
- rebuild

* Wed Mar 23 2005 Guillaume Rousse <guillomovitch@mandrake.org> 0.3.5-1mdk 
- first mdk release
