%define name	lockfile-progs
%define version	0.1.10
%define release	%mkrel 7

Summary:	Programs for locking and unlocking files and mailboxes
Name:		%{name}
Version:	%{version}
Release:	%mkrel 6
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


