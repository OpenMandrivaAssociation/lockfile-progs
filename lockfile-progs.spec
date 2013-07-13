Summary:	Programs for locking and unlocking files and mailboxes
Name:		lockfile-progs
Version:	0.1.10
Release:	9
License:	GPLv2
Group:		System/Base
Url:		http://packages.qa.debian.org/lockfile-progs
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
%apply_patches

%build
%make CFLAGS="%{optflags}"

%install
mkdir -p %{buildroot}%{_mandir}
cp -a bin %{buildroot}%{_bindir}
cp -a man %{buildroot}%{_mandir}/man1

%files
%doc TODO debian/changelog
%{_bindir}/lockfile-create
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

