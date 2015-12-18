%define desktop_file_utils_version 0.2.93

Summary: mlterm(Multi Lingual TERMinal emulator)
URL:     http://sourceforge.net/projects/mlterm/
Name: mlterm-gtk3
Version: 3.6.1
Release: 1%{?dist}
Epoch: 1
License: BSD License

# Reserve 1-9 number for other srcs.
Source0: http://downloads.sourceforge.net/project/mlterm/01release/mlterm-%{version}/mlterm-%{version}.tar.gz
Source10: %{name}.desktop

Buildroot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

# desktopfile
BuildRequires: desktop-file-utils >= %{desktop_file_utils_version}

BuildRequires: gettext libXt-devel cairo-devel gdk-pixbuf2-devel fribidi-devel gtk3-devel
Requires: libXt cairo gdk-pixbuf2 fribidi gtk3 gnome-icon-theme
Provides: %{_bindir}/mlterm
Provides: %{_bindir}/mlcc
Provides: %{_bindir}/mlclient
Provides: %{_bindir}/mlclientx
Provides: %{_libexecdir}/mlterm/mlconfig
Provides: %{_libexecdir}/mlterm/mlimgloader
Provides: %{_libexecdir}/mlterm/mlterm-menu

%description
mlterm is a multi-lingual terminal emulator , which supports
various character sets and encodings in the world.

%prep
%setup -q -b 0 -n mlterm-%{version}

%build
%configure \
  --prefix=%{buildroot} \
  --enable-uim \
  --enable-m17nlib \
  --enable-ibus \
  --enable-fcitx \
  --enable-scim \
  --enable-canna \
  --enable-wnn \
  --enable-vt52 \
  --disable-utmp \
  --enable-optimize-redrawing \
  --with-gtk=3.0 \
  --with-imagelib=gdk-pixbuf \
  --with-scrollbars=sample,extra,pixmap_engine

make %{?_smp_mflags}

%install
[ -d %{buildroot} ] && rm -rf %{buildroot}
mkdir %{buildroot}
make install DESTDIR=%{buildroot}
mkdir -p %{buildroot}/%{_datadir}/applications
desktop-file-install \
    --dir %{buildroot}/%{_datadir}/applications \
    %{SOURCE10}

%post
update-desktop-database &> /dev/null ||:

%postun
update-desktop-database &> /dev/null ||:

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/mlcc
%{_bindir}/mlclient
%{_bindir}/mlclientx
%{_bindir}/mlterm
%config(noreplace) %{_sysconfdir}/mlterm/aafont
%config(noreplace) %{_sysconfdir}/mlterm/color
%config(noreplace) %{_sysconfdir}/mlterm/font
%config(noreplace) %{_sysconfdir}/mlterm/font-fb
%config(noreplace) %{_sysconfdir}/mlterm/key
%config(noreplace) %{_sysconfdir}/mlterm/main
%config(noreplace) %{_sysconfdir}/mlterm/menu
%config(noreplace) %{_sysconfdir}/mlterm/taafont
%config(noreplace) %{_sysconfdir}/mlterm/termcap
%config(noreplace) %{_sysconfdir}/mlterm/tfont
%config(noreplace) %{_sysconfdir}/mlterm/vaafont
%config(noreplace) %{_sysconfdir}/mlterm/vfont
%config(noreplace) %{_sysconfdir}/mlterm/xim
%{_libdir}/libkik.a
%{_libdir}/libkik.la
%{_libdir}/libkik.so
%{_libdir}/libkik.so.16
%{_libdir}/libkik.so.16.0.0
%{_libdir}/libmkf.a
%{_libdir}/libmkf.la
%{_libdir}/libmkf.so
%{_libdir}/libmkf.so.16
%{_libdir}/libmkf.so.16.0.1
%{_libdir}/libmlterm_core.a
%{_libdir}/libmlterm_core.la
%{_libdir}/libmlterm_core.so
%{_libdir}/mkf/*
%{_libdir}/mlterm/*
%{_libexecdir}/mlterm/*
%{_mandir}/man1/mlclient.*
%{_mandir}/man1/mlterm.*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/mlterm/scrollbars/sample3/*
%{_datadir}/locale/ar/LC_MESSAGES/mlconfig.mo
%{_datadir}/locale/de/LC_MESSAGES/mlconfig.mo
%{_datadir}/locale/ja/LC_MESSAGES/mlconfig.mo
%{_datadir}/locale/vi/LC_MESSAGES/mlconfig.mo
%{_datadir}/locale/zh_TW/LC_MESSAGES/mlconfig.mo

%changelog
* Wed Dec 16 2015 Tomohiro NAKAMURA <quickness.net@gmail.com> 3.6.0-1
- create spec file and build it
