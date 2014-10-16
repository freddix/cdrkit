Summary:	A command line CD/DVD-Recorder
Name:		cdrkit
Version:	1.1.11
Release:	5
License:	GPL v2
Group:		Applications/System
Source0:	http://cdrkit.org/releases/%{name}-%{version}.tar.gz
# Source0-md5:	efe08e2f3ca478486037b053acd512e9
URL:		http://cdrkit.org/
BuildRequires:	cmake
BuildRequires:	libcap-devel
BuildRequires:	libmagic-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Cdrkit allows you to create CD's on a CD-Recorder (SCSI/ATAPI).
Supports data, audio, mixed, multi-session and CD+ discs etc.

%package devel
Summary:	cdrkit header files and schily library
Group:		Development/Libraries

%description devel
cdrkit header files and schily library.

%prep
%setup -q

%build
%{__make}			\
	CC="%{__cc}"		\
	CFLAGS="%{rpmcflags}"	\
	LDFLAGS="%{rpmldflags}"	\
	VERBOSE=1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{_libdir},%{_includedir}/cdrkit/usal}
%{__cmake} -DCMAKE_INSTALL_PREFIX=$RPM_BUILD_ROOT%{_prefix} build

%{__make} install

install build/*/*.a $RPM_BUILD_ROOT%{_libdir}
install include/*.h $RPM_BUILD_ROOT%{_includedir}/cdrkit
install include/usal/*.h $RPM_BUILD_ROOT%{_includedir}/cdrkit/usal
install wodim/wodim.dfl $RPM_BUILD_ROOT%{_sysconfdir}/wodim.conf

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/READMEs/*
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/wodim.conf
%attr(755,root,cdrom) %{_bindir}/wodim
%attr(755,root,root) %{_sbindir}/netscsid
%{_mandir}/man1/wodim.1*

# icedax (cdda2wav)
%defattr(644,root,root,755)
%doc doc/icedax/*
%attr(755,root,root) %{_bindir}/cdda2mp3
%attr(755,root,root) %{_bindir}/cdda2ogg
%attr(755,root,root) %{_bindir}/icedax
%attr(755,root,root) %{_bindir}/pitchplay
%attr(755,root,root) %{_bindir}/readmult
%{_mandir}/man1/cdda2ogg.1*
%{_mandir}/man1/icedax.1*
%{_mandir}/man1/pitchplay.1*
%{_mandir}/man1/readmult.1*

# readcd
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/readom
%{_mandir}/man1/readom.1*

# utils
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/devdump
%attr(755,root,root) %{_bindir}/dirsplit
%attr(755,root,root) %{_bindir}/isodebug
%attr(755,root,root) %{_bindir}/isoinfo
%attr(755,root,root) %{_bindir}/isovfy
%attr(755,root,root) %{_bindir}/isodump
%{_mandir}/man1/dirsplit.1*
%{_mandir}/man1/devdump.1*
%{_mandir}/man1/isodebug.1*
%{_mandir}/man1/isodump.1*
%{_mandir}/man1/isoinfo.1*
%{_mandir}/man1/isovfy.1*

# genisoimage (mkisofs)
%defattr(644,root,root,755)
%doc doc/genisoimage/*
%attr(755,root,root) %{_bindir}/genisoimage
%{_mandir}/man1/genisoimage.1*
%{_mandir}/man5/genisoimagerc.5*

%files devel
%defattr(644,root,root,755)
%{_libdir}/lib*.a
%{_includedir}/cdrkit

