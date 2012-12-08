%define name	lockfile-progs
%define version	0.1.10
%define release	%mkrel 7

Summary:	Programs for locking and unlocking files and mailboxes
Name:		%{name}
Version:	%{version}
Release:	%mkrel 8
License:	GPL
Group:		System/Base
URL:		http://packages.qa.debian.org/lockfile-progs
BuildRoot:	%_tmppath/%{name}-%{version}-root-%(id -u -n)
Source0:	http://ftp.debian.org/debian/pool/main/l/lockfile-progs/lockfile-progs_0.1.10.tar.bz2
# http://bugs.debian.org/cgi-bin/bugreport.cgi/diff.out?bug=244314;msg=10;att=1
Patch0:		lockfile-progs-0.1.10.manpage.patch
Patch1:		lockfile-progs-0.1.10-fix-str-fmt.patch
BuildRequires:	lockfile-devel

%description
This package includes several programs to safely lock and unlock files and
mailboxes from the command line.

%prep 
%setup -q
%patch0 -p1 -b .orig
%patch1 -p0 -b .str

%build
%make CFLAGS="%{optflags}"

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_mandir}
cp -a bin $RPM_BUILD_ROOT%{_bindir}
cp -a man $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc TODO debian/changelog
%attr(755,root,root) %{_bindir}/lockfile-create
%{_bindir}/lockfile-remove
%{_bindir}/lockfile-touch
%attr(2755,root,mail) %{_bindir}/mail-lock
%{_bindir}/mail-touchlock
%{_bindir}/mail-unlock
%{_mandir}/man1/lockfile-progs.1*
%{_mandir}/man1/lockfile-create.1*
%{_mandir}/man1/lockfile-remove.1*
%{_mandir}/man1/lockfile-touch.1*
%{_mandir}/man1/mail-lock.1*
%{_mandir}/man1/mail-touchlock.1*
%{_mandir}/man1/mail-unlock.1*




%changelog
* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0.1.10-6mdv2011.0
+ Revision: 666090
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 0.1.10-5mdv2011.0
+ Revision: 606416
- rebuild

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 0.1.10-4mdv2010.1
+ Revision: 523191
- rebuilt for 2010.1

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 0.1.10-3mdv2010.0
+ Revision: 426002
- rebuild

* Fri Apr 10 2009 Funda Wang <fwang@mandriva.org> 0.1.10-3mdv2009.1
+ Revision: 365707
- fix str fmt

* Mon Jul 28 2008 Thierry Vignaud <tv@mandriva.org> 0.1.10-3mdv2009.0
+ Revision: 251325
- rebuild

* Thu Jan 03 2008 Olivier Blin <oblin@mandriva.com> 0.1.10-1mdv2008.1
+ Revision: 140932
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Thu Aug 10 2006 Luca Berra <bluca@comedia.it>
+ 08/10/06 07:56:05 (55306)
Import lockfile-progs

* Wed Aug 09 2006 Luca Berra <bluca@mandriva.org> 0.1.10-1mdv2007.0
- Initial mandriva package

